import Link from "next/link";

function Navbar() {
    return (
        <nav>
            <h1>Helpdesk</h1>
            <div className="flex gap-3">
                <Link href="/">Dashboard</Link>
                <Link href="/news">News</Link>
                <Link href="/news/latest">Latest News</Link>
                <Link href="/tickets">Tickets</Link>
                <Link href="/books">Books</Link>
            </div>
        </nav>
    )
}

export default Navbar