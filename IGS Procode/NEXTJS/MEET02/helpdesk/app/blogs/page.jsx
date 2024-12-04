import styles from "../styles/Blogs.module.css";
import Link from "next/link";

async function getUsers() {
  const users = [
    { id: 1, name: "Leanne Graham" },
    { id: 2, name: "Ervin Howell" },
    { id: 3, name: "Clementine Bauch" },
    { id: 4, name: "Patricia Lebsack" },
    { id: 5, name: "Chelsey Dietrich" },
    { id: 6, name: "Mrs. Dennis Schulist" },
    { id: 7, name: "Kurtis Weissnat" },
    { id: 8, name: "Nicholas Runolfsdottir V" },
    { id: 9, name: "Glenna Reichert" },
    { id: 10, name: "Clementina DuBuque" },
  ];
  return users;
}

export default async function BlogsPage() {
  const users = await getUsers();
  return (
    <section className="blog">
      <h1>Blogs</h1>
      {users?.map((user) => (
        <Link href={`/blogs/${user.id}`} key={user.id} className={styles.single}>
          <h2>{user.name}</h2>
        </Link>
      ))}
    </section>
  );
}
