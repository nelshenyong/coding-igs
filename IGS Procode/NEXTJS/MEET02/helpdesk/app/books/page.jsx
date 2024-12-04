import clientPromise from '@/lib/mongodb';
import Link from 'next/link';

async function getBooks() {
  const client = await clientPromise;
  const db = client.db('bookstore');
  const books = await db.collection('books').find({}).toArray();
  return JSON.parse(JSON.stringify(books));
}

export default async function BooksPage() {
  const books = await getBooks();
  console.log('Books fetched on page:', books);
  return (
    <section className="blog">
      <h1>Books</h1>
      {books.length === 0 ? (
        <p>No books available</p>
      ) : (
        <ul>
          {books.map((book) => (
            <li key={book._id}>
              <Link href={`/books/${book._id}`}>{book.title}</Link>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
