import { Inter } from 'next/font/google'
import Link from 'next/link'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
  <div class="flex h-screen items-center justify-center">
    <div class="flex flex-col space-y-4">
      <Link
        href="/login"
        className="w-full px-4 py-2 bg-blue-600 text-white font-medium rounded-lg shadow-md hover:bg-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2"
      >
        Login
      </Link>
      <Link
        href="/signup"
        className="w-full px-4 py-2 bg-blue-600 text-white font-medium rounded-lg shadow-md hover:bg-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2"
      >
        Sign Up
      </Link>
    </div>
  </div>
</>

  )
}
