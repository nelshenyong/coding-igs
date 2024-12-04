export default function BookPage({ params }) {
    const { id } = params;
    const { title } = params;
  
    return (
      <div>
        <h1>Book ID: {id}</h1>
        <h1>Book Title: {title}</h1>
      </div>
    );
  }
  