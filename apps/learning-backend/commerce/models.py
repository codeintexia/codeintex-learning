import uuid

from django.conf import settings
from django.db import models
from django.db.models import F, Q

from learning.models import Course


class CourseOffer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="commerce_offers",
    )
    amount_minor = models.PositiveBigIntegerField()
    currency = models.CharField(
        max_length=3,
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(amount_minor__gt=0),
                name="commerce_offer_amount_gt_zero",
            ),
            models.UniqueConstraint(
                fields=["course", "currency"],
                condition=Q(is_active=True),
                name="unique_active_offer_per_course_currency",
            ),
        ]

    def save(self, *args, **kwargs):
        if self.pk:
            persisted = (
                type(self)
                .objects
                .filter(pk=self.pk)
                .values(
                    "course_id",
                    "amount_minor",
                    "currency",
                )
                .first()
            )

            if persisted is not None:
                immutable_values = {
                    "course_id": self.course_id,
                    "amount_minor": self.amount_minor,
                    "currency": self.currency,
                }

                if immutable_values != persisted:
                    raise ValueError(
                        "CourseOffer commercial identity is immutable."
                    )

        return super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.course.title} · "
            f"{self.currency} {self.amount_minor}"
        )


class Order(models.Model):
    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        FULFILLED = "FULFILLED", "Fulfilled"
        CANCELLED = "CANCELLED", "Cancelled"
        EXPIRED = "EXPIRED", "Expired"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="commerce_orders",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="commerce_orders",
    )
    offer = models.ForeignKey(
        CourseOffer,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.OPEN,
    )
    subtotal_amount_minor = models.PositiveBigIntegerField()
    discount_amount_minor = models.PositiveBigIntegerField(
        default=0,
    )
    total_amount_minor = models.PositiveBigIntegerField()
    currency = models.CharField(
        max_length=3,
    )
    course_title_snapshot = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    expires_at = models.DateTimeField()
    fulfilled_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    cancelled_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    status__in=[
                        "OPEN",
                        "FULFILLED",
                        "CANCELLED",
                        "EXPIRED",
                    ]
                ),
                name="commerce_order_valid_status",
            ),
            models.CheckConstraint(
                condition=Q(
                    discount_amount_minor__lte=F(
                        "subtotal_amount_minor"
                    )
                ),
                name="commerce_order_discount_lte_subtotal",
            ),
            models.CheckConstraint(
                condition=Q(
                    total_amount_minor=(
                        F("subtotal_amount_minor")
                        - F("discount_amount_minor")
                    )
                ),
                name="commerce_order_total_consistent",
            ),
            models.CheckConstraint(
                condition=Q(total_amount_minor__gt=0),
                name="commerce_order_total_gt_zero",
            ),
            models.UniqueConstraint(
                fields=["learner", "course"],
                condition=Q(status="OPEN"),
                name="unique_open_order_per_learner_course",
            ),
        ]

    def save(self, *args, **kwargs):
        if self.pk:
            persisted = (
                type(self)
                .objects
                .filter(pk=self.pk)
                .values(
                    "learner_id",
                    "course_id",
                    "offer_id",
                    "subtotal_amount_minor",
                    "discount_amount_minor",
                    "total_amount_minor",
                    "currency",
                    "course_title_snapshot",
                )
                .first()
            )

            if persisted is not None:
                immutable_values = {
                    "learner_id": self.learner_id,
                    "course_id": self.course_id,
                    "offer_id": self.offer_id,
                    "subtotal_amount_minor": self.subtotal_amount_minor,
                    "discount_amount_minor": self.discount_amount_minor,
                    "total_amount_minor": self.total_amount_minor,
                    "currency": self.currency,
                    "course_title_snapshot": self.course_title_snapshot,
                }

                if immutable_values != persisted:
                    raise ValueError(
                        "Order commercial snapshot is immutable."
                    )

        return super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.learner} · "
            f"{self.course_title_snapshot} · "
            f"{self.status}"
        )

class Payment(models.Model):
    class Status(models.TextChoices):
        CREATED = "CREATED", "Created"
        PENDING = "PENDING", "Pending"
        SUCCEEDED = "SUCCEEDED", "Succeeded"
        FAILED = "FAILED", "Failed"
        CANCELLED = "CANCELLED", "Cancelled"
        EXPIRED = "EXPIRED", "Expired"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name="payments",
    )
    provider = models.CharField(
        max_length=64,
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.CREATED,
    )
    operation_key = models.UUIDField(
        unique=True,
    )
    merchant_reference = models.CharField(
        max_length=128,
        unique=True,
    )
    provider_transaction_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    amount_minor = models.PositiveBigIntegerField()
    currency = models.CharField(
        max_length=3,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    succeeded_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    status__in=[
                        "CREATED",
                        "PENDING",
                        "SUCCEEDED",
                        "FAILED",
                        "CANCELLED",
                        "EXPIRED",
                    ]
                ),
                name="commerce_payment_valid_status",
            ),
            models.CheckConstraint(
                condition=Q(amount_minor__gt=0),
                name="commerce_payment_amount_gt_zero",
            ),
            models.UniqueConstraint(
                fields=["provider", "provider_transaction_id"],
                condition=Q(provider_transaction_id__isnull=False),
                name="unique_payment_provider_transaction",
            ),
            models.UniqueConstraint(
                fields=["order"],
                condition=Q(
                    status__in=[
                        "CREATED",
                        "PENDING",
                    ]
                ),
                name="unique_payable_payment_per_order",
            ),
        ]

    def __str__(self):
        return (
            f"{self.provider} · "
            f"{self.merchant_reference} · "
            f"{self.status}"
        )

class ProviderEvent(models.Model):
    class ProcessingStatus(models.TextChoices):
        RECEIVED = "RECEIVED", "Received"
        PROCESSING = "PROCESSING", "Processing"
        PROCESSED = "PROCESSED", "Processed"
        FAILED = "FAILED", "Failed"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    provider = models.CharField(
        max_length=64,
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.PROTECT,
        related_name="provider_events",
        null=True,
        blank=True,
    )
    merchant_reference = models.CharField(
        max_length=128,
    )
    provider_event_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    provider_transaction_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    event_type = models.CharField(
        max_length=128,
    )
    provider_status = models.CharField(
        max_length=128,
    )
    observed_payment_status = models.CharField(
        max_length=16,
        choices=Payment.Status.choices,
        null=True,
        blank=True,
    )
    adjustment_kind = models.CharField(
        max_length=16,
        null=True,
        blank=True,
    )
    adjustment_cumulative_amount_minor = models.PositiveBigIntegerField(
        null=True,
        blank=True,
    )
    provider_adjustment_reference = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    adjustment_confirmed = models.BooleanField(
        default=False,
    )
    is_partial_adjustment = models.BooleanField(
        default=False,
    )
    amount_minor = models.PositiveBigIntegerField(
        null=True,
        blank=True,
    )
    currency = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )
    payload_digest = models.CharField(
        max_length=128,
    )
    authenticity_verified_at = models.DateTimeField()
    authenticity_method = models.CharField(
        max_length=128,
    )
    processing_status = models.CharField(
        max_length=16,
        choices=ProcessingStatus.choices,
        default=ProcessingStatus.RECEIVED,
    )
    attempt_count = models.PositiveIntegerField(
        default=0,
    )
    last_error_code = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    processed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    processing_status__in=[
                        "RECEIVED",
                        "PROCESSING",
                        "PROCESSED",
                        "FAILED",
                    ]
                ),
                name="commerce_event_valid_processing_status",
            ),
            models.UniqueConstraint(
                fields=["provider", "provider_event_id"],
                condition=Q(provider_event_id__isnull=False),
                name="unique_provider_event_identity",
            ),
        ]

    def __str__(self):
        return (
            f"{self.provider} · "
            f"{self.event_type} · "
            f"{self.processing_status}"
        )

class FinancialAdjustment(models.Model):
    class Kind(models.TextChoices):
        REFUND = "REFUND", "Refund"
        REVERSAL = "REVERSAL", "Reversal"
        CHARGEBACK = "CHARGEBACK", "Chargeback"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        FAILED = "FAILED", "Failed"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.PROTECT,
        related_name="financial_adjustments",
    )
    kind = models.CharField(
        max_length=16,
        choices=Kind.choices,
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.PENDING,
    )
    amount_minor = models.PositiveBigIntegerField()
    currency = models.CharField(
        max_length=3,
    )
    operation_key = models.UUIDField(
        null=True,
        blank=True,
    )
    provider_reference = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    initiated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="initiated_financial_adjustments",
        null=True,
        blank=True,
    )
    initiation_reason = models.TextField(
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    confirmed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    kind__in=[
                        "REFUND",
                        "REVERSAL",
                        "CHARGEBACK",
                    ]
                ),
                name="commerce_adjustment_valid_kind",
            ),
            models.CheckConstraint(
                condition=Q(
                    status__in=[
                        "PENDING",
                        "CONFIRMED",
                        "FAILED",
                    ]
                ),
                name="commerce_adjustment_valid_status",
            ),
            models.CheckConstraint(
                condition=Q(amount_minor__gt=0),
                name="commerce_adjustment_amount_gt_zero",
            ),
            models.UniqueConstraint(
                fields=["operation_key"],
                condition=Q(operation_key__isnull=False),
                name="unique_adjustment_operation_key",
            ),
            models.UniqueConstraint(
                fields=["payment", "provider_reference"],
                condition=Q(provider_reference__isnull=False),
                name="unique_adjustment_provider_reference",
            ),
        ]

    def __str__(self):
        return (
            f"{self.kind} · "
            f"{self.amount_minor} {self.currency} · "
            f"{self.status}"
        )

class PaymentIntegrityCase(models.Model):
    class Reason(models.TextChoices):
        AMOUNT_MISMATCH = (
            "AMOUNT_MISMATCH",
            "Amount mismatch",
        )
        CURRENCY_MISMATCH = (
            "CURRENCY_MISMATCH",
            "Currency mismatch",
        )
        PROVIDER_IDENTITY_MISMATCH = (
            "PROVIDER_IDENTITY_MISMATCH",
            "Provider identity mismatch",
        )
        LATE_PAYMENT_CLOSED_ORDER = (
            "LATE_PAYMENT_CLOSED_ORDER",
            "Late payment against closed order",
        )
        MULTIPLE_SUCCESSFUL_PAYMENTS = (
            "MULTIPLE_SUCCESSFUL_PAYMENTS",
            "Multiple successful payments",
        )
        PARTIAL_CHARGEBACK = (
            "PARTIAL_CHARGEBACK",
            "Partial chargeback",
        )
        FULFILLMENT_INCONSISTENCY = (
            "FULFILLMENT_INCONSISTENCY",
            "Fulfillment inconsistency",
        )

    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        RESOLVED = "RESOLVED", "Resolved"

    class Resolution(models.TextChoices):
        FULFILL = "FULFILL", "Fulfill"
        REFUND = "REFUND", "Refund"
        KEEP_ACCESS = "KEEP_ACCESS", "Keep access"
        REVOKE_PURCHASE_ACCESS = (
            "REVOKE_PURCHASE_ACCESS",
            "Revoke purchase access",
        )
        NO_ACTION = "NO_ACTION", "No action"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name="payment_integrity_cases",
        null=True,
        blank=True,
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.PROTECT,
        related_name="integrity_cases",
        null=True,
        blank=True,
    )
    provider_event = models.ForeignKey(
        ProviderEvent,
        on_delete=models.PROTECT,
        related_name="integrity_cases",
        null=True,
        blank=True,
    )
    case_key = models.CharField(
        max_length=255,
        unique=True,
    )
    reason = models.CharField(
        max_length=64,
        choices=Reason.choices,
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.OPEN,
    )
    resolution = models.CharField(
        max_length=32,
        choices=Resolution.choices,
        null=True,
        blank=True,
    )
    resolution_reason = models.TextField(
        blank=True,
    )
    opened_at = models.DateTimeField(
        auto_now_add=True,
    )
    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    resolved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="resolved_payment_integrity_cases",
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    reason__in=[
                        "AMOUNT_MISMATCH",
                        "CURRENCY_MISMATCH",
                        "PROVIDER_IDENTITY_MISMATCH",
                        "LATE_PAYMENT_CLOSED_ORDER",
                        "MULTIPLE_SUCCESSFUL_PAYMENTS",
                        "PARTIAL_CHARGEBACK",
                        "FULFILLMENT_INCONSISTENCY",
                    ]
                ),
                name="commerce_integrity_case_valid_reason",
            ),
            models.CheckConstraint(
                condition=Q(
                    status__in=[
                        "OPEN",
                        "RESOLVED",
                    ]
                ),
                name="commerce_integrity_case_valid_status",
            ),
            models.CheckConstraint(
                condition=(
                    Q(order__isnull=False)
                    | Q(payment__isnull=False)
                    | Q(provider_event__isnull=False)
                ),
                name="commerce_integrity_case_has_reference",
            ),
            models.CheckConstraint(
                condition=(
                    Q(resolution__isnull=True)
                    | Q(
                        resolution__in=[
                            "FULFILL",
                            "REFUND",
                            "KEEP_ACCESS",
                            "REVOKE_PURCHASE_ACCESS",
                            "NO_ACTION",
                        ]
                    )
                ),
                name="commerce_integrity_case_valid_resolution",
            ),
        ]

    def __str__(self):
        return (
            f"{self.case_key} · "
            f"{self.reason} · "
            f"{self.status}"
        )

class CourseEntitlement(models.Model):
    class Source(models.TextChoices):
        PURCHASE = "PURCHASE", "Purchase"
        SCHOLARSHIP = "SCHOLARSHIP", "Scholarship"
        ADMIN_GRANT = "ADMIN_GRANT", "Admin grant"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        REVOKED = "REVOKED", "Revoked"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="course_entitlements",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="entitlements",
    )
    source = models.CharField(
        max_length=16,
        choices=Source.choices,
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name="course_entitlements",
        null=True,
        blank=True,
    )
    granted_at = models.DateTimeField(
        auto_now_add=True,
    )
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="granted_course_entitlements",
        null=True,
        blank=True,
    )
    grant_reason = models.TextField(
        blank=True,
    )
    revoked_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    revoked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="revoked_course_entitlements",
        null=True,
        blank=True,
    )
    revocation_reason = models.TextField(
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    source__in=[
                        "PURCHASE",
                        "SCHOLARSHIP",
                        "ADMIN_GRANT",
                    ]
                ),
                name="commerce_entitlement_valid_source",
            ),
            models.CheckConstraint(
                condition=Q(
                    status__in=[
                        "ACTIVE",
                        "REVOKED",
                    ]
                ),
                name="commerce_entitlement_valid_status",
            ),
            models.CheckConstraint(
                condition=(
                    Q(source="PURCHASE", order__isnull=False)
                    | Q(
                        source__in=[
                            "SCHOLARSHIP",
                            "ADMIN_GRANT",
                        ],
                        order__isnull=True,
                    )
                ),
                name="commerce_entitlement_source_order_consistent",
            ),
            models.UniqueConstraint(
                fields=["order"],
                condition=Q(order__isnull=False),
                name="unique_entitlement_per_order",
            ),
            models.UniqueConstraint(
                fields=["learner", "course"],
                condition=Q(
                    source="PURCHASE",
                    status="ACTIVE",
                ),
                name="unique_active_purchase_entitlement",
            ),
        ]

    def __str__(self):
        return (
            f"{self.learner} · "
            f"{self.course.title} · "
            f"{self.source} · "
            f"{self.status}"
        )
