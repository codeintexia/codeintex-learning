"use client"

import { useState } from 'react'
import Link from 'next/link'

const courses = [
  {
    id: 1,
    title: "Human-Centered AI — Foundations",
    category: "literacy",
    categoryLabel: "Literacy",
    description: "Merancang sistem AI yang benar-benar bekerja untuk manusia.",
    duration: "6 Jam",
    lessons: "25 Lesson",
    modules: "6 Modul",
    isLive: true,
    href: "/courses/hcai-foundations",
    statusText: "Tersedia Sekarang",
  },
  {
    id: 2,
    title: "AI untuk Proses Data",
    category: "competency",
    categoryLabel: "Competency",
    description: "Membersihkan, memodelkan, dan mengevaluasi data riset dengan pendekatan AI.",
    isLive: false,
    statusText: "Segera Hadir",
  },
  {
    id: 3,
    title: "AI untuk Pengalaman Pelanggan",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan.",
    isLive: false,
    statusText: "Segera Hadir",
  },
  {
    id: 4,
    title: "AI untuk Keamanan Informasi",
    category: "competency",
    categoryLabel: "Competency",
    description: "Materi sedang dalam pengembangan.",
    isLive: false,
    statusText: "Segera Hadir",
  },
]

const tabs = [
  { id: 'all', label: 'Semua Program' },
  { id: 'literacy', label: 'Literacy' },
  { id: 'competency', label: 'Competency' },
]

const partners = ['Universitas Indonesia', 'ITB', 'BRIN', 'Kemenristek', 'UGM', 'IPB']

export default function HomePage() {
  const [activeTab, setActiveTab] = useState('all')

  const filteredCourses = courses.filter((course) =>
    activeTab === 'all' ? true : course.category === activeTab
  )

  return (
    <div className="flex flex-col items-stretch bg-white">
      {/* Hero */}
      <section className="relative bg-[#02040B] overflow-hidden">
        <div
          className="absolute inset-0 opacity-[0.15]"
          style={{
            backgroundImage:
              'linear-gradient(#1a2233 1px, transparent 1px), linear-gradient(90deg, #1a2233 1px, transparent 1px)',
            backgroundSize: '48px 48px',
          }}
        />
        <div className="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-20 sm:py-28 text-center">
          <span className="inline-block text-[12px] font-semibold text-[#02B3E4] uppercase tracking-[0.12em] mb-5">
            Program Bersertifikat
          </span>
          <h1 className="text-[36px] sm:text-[52px] font-extrabold tracking-tight text-white leading-[1.1] max-w-4xl mx-auto mb-6">
            Kuasai AI yang benar-benar dipakai di dunia nyata
          </h1>
          <p className="text-[16px] sm:text-[18px] text-[#B5BAC6] max-w-2xl mx-auto leading-relaxed mb-10">
            Kurikulum berbasis riset akademis, dibimbing praktisi, dirancang untuk hasil yang bisa langsung
            diterapkan ke pekerjaan atau penelitian kamu.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              href="/courses/hcai-foundations"
              className="inline-flex items-center justify-center rounded-[4px] bg-[#02B3E4] text-[#02040B] px-8 py-4 text-[15px] font-bold hover:bg-[#3ac4ec] transition-colors w-full sm:w-auto"
            >
              Mulai Belajar Gratis
            </Link>
            <button
              onClick={() => document.getElementById('programs')?.scrollIntoView({ behavior: 'smooth' })}
              className="inline-flex items-center justify-center rounded-[4px] border border-white/20 text-white px-8 py-4 text-[15px] font-bold hover:bg-white/5 transition-colors w-full sm:w-auto"
            >
              Lihat Semua Program
            </button>
          </div>
        </div>

        {/* Stats bar */}
        <div className="relative border-t border-white/10 bg-black/20">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div>
              <span className="block text-[28px] font-extrabold text-white">6</span>
              <span className="text-[12px] text-[#8890A0] uppercase tracking-wide">Modul</span>
            </div>
            <div>
              <span className="block text-[28px] font-extrabold text-white">25</span>
              <span className="text-[12px] text-[#8890A0] uppercase tracking-wide">Lesson</span>
            </div>
            <div>
              <span className="block text-[28px] font-extrabold text-white">100%</span>
              <span className="text-[12px] text-[#8890A0] uppercase tracking-wide">Gratis & Terbuka</span>
            </div>
            <div>
              <span className="block text-[28px] font-extrabold text-white">6 Jam</span>
              <span className="text-[12px] text-[#8890A0] uppercase tracking-wide">Estimasi Belajar</span>
            </div>
          </div>
        </div>
      </section>

      {/* Partner strip */}
      <section id="partners" className="border-b border-[#EAEDF2] py-8">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <p className="text-center text-[11px] font-semibold text-[#8890A0] uppercase tracking-[0.1em] mb-6">
            Dipercaya peneliti dari
          </p>
          <div className="flex flex-wrap items-center justify-center gap-x-10 gap-y-4">
            {partners.map((p) => (
              <span key={p} className="text-[14px] font-semibold text-[#4A4F5A]">{p}</span>
            ))}
          </div>
        </div>
      </section>

      {/* Programs */}
      <section id="programs" className="py-20 bg-white">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-[32px] font-extrabold tracking-tight text-[#02040B] mb-4">
              Pilih program yang sesuai tujuanmu
            </h2>
            <div className="inline-flex flex-wrap justify-center bg-[#F3F4F7] rounded-[8px] p-1 gap-1">
              {tabs.map((tab) => (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`px-5 py-2 rounded-[6px] text-[13px] font-semibold transition-colors ${
                    activeTab === tab.id
                      ? 'bg-white text-[#02040B] shadow-sm'
                      : 'text-[#6B7280] hover:text-[#02040B]'
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredCourses.map((course) =>
              course.isLive ? (
                <Link
                  key={course.id}
                  href={course.href || '#'}
                  className="group flex flex-col justify-between rounded-[8px] border border-[#EAEDF2] bg-white overflow-hidden hover:shadow-[0_12px_32px_rgba(2,4,11,0.1)] hover:-translate-y-1 transition-all duration-200"
                >
                  <div className="h-1.5 w-full bg-[#02B3E4]" />
                  <div className="p-6 flex-grow flex flex-col justify-between">
                    <div>
                      <span className="inline-block bg-[#E6F8FE] text-[#0284B8] text-[10px] font-bold uppercase tracking-wide py-1 px-2.5 rounded-full mb-3">
                        {course.categoryLabel}
                      </span>
                      <h3 className="text-[17px] font-bold text-[#02040B] mb-2 leading-snug group-hover:text-[#02B3E4] transition-colors">
                        {course.title}
                      </h3>
                      <p className="text-[13px] text-[#6B7280] leading-relaxed mb-4">{course.description}</p>
                      <div className="flex flex-wrap gap-3 text-[12px] text-[#8890A0] font-medium">
                        <span>{course.modules}</span>
                        <span>{course.lessons}</span>
                        <span>{course.duration}</span>
                      </div>
                    </div>
                    <div className="mt-6 pt-4 border-t border-[#F3F4F7] flex items-center justify-between">
                      <span className="bg-[#E6F8FE] text-[#0284B8] text-[11px] font-bold py-1 px-3 rounded-full">
                        {course.statusText}
                      </span>
                      <span className="text-[#02B3E4] text-[13px] font-bold">
                        Mulai →
                      </span>
                    </div>
                  </div>
                </Link>
              ) : (
                <div
                  key={course.id}
                  className="flex flex-col justify-between rounded-[8px] border border-[#EAEDF2] bg-[#FAFAFB] opacity-80 overflow-hidden"
                >
                  <div className="h-1.5 w-full bg-[#D9DCE3]" />
                  <div className="p-6 flex-grow flex flex-col justify-between">
                    <div>
                      <span className="inline-block bg-[#EEF0F3] text-[#8890A0] text-[10px] font-bold uppercase tracking-wide py-1 px-2.5 rounded-full mb-3">
                        {course.categoryLabel}
                      </span>
                      <h3 className="text-[17px] font-bold text-[#4A4F5A] mb-2 leading-snug">{course.title}</h3>
                      <p className="text-[13px] text-[#8890A0] leading-relaxed">{course.description}</p>
                    </div>
                    <div className="mt-6 pt-4 border-t border-[#F3F4F7] flex items-center justify-between">
                      <span className="bg-[#FEF3C7] text-[#92700E] text-[11px] font-bold py-1 px-3 rounded-full">
                        {course.statusText}
                      </span>
                    </div>
                  </div>
                </div>
              )
            )}
          </div>
        </div>
      </section>

      {/* Testimonial */}
      <section className="py-20 bg-[#02040B]">
        <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-[22px] sm:text-[26px] font-medium text-white leading-relaxed mb-8">
            "Kurikulumnya langsung bisa dipakai untuk audit sistem AI yang sedang saya kerjakan — bukan
            teori kosong."
          </p>
          <p className="text-[14px] font-semibold text-white">Peneliti, Fakultas Ilmu Komputer</p>
          <p className="text-[13px] text-[#8890A0]">Peserta Human-Centered AI — Foundations</p>
        </div>
      </section>

      {/* Final CTA */}
      <section className="py-20 bg-white">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center rounded-[12px] bg-[#F3F4F7] py-14 px-8">
          <h2 className="text-[26px] font-extrabold text-[#02040B] mb-3">Siap mulai belajar?</h2>
          <p className="text-[15px] text-[#6B7280] mb-8 max-w-md mx-auto">
            Gratis, terbuka, dan bisa langsung diterapkan ke pekerjaan atau riset kamu hari ini.
          </p>
          <Link
            href="/courses/hcai-foundations"
            className="inline-flex items-center justify-center rounded-[4px] bg-[#02B3E4] text-[#02040B] px-8 py-4 text-[15px] font-bold hover:bg-[#3ac4ec] transition-colors"
          >
            Mulai Belajar Gratis
          </Link>
        </div>
      </section>
    </div>
  )
}
