import Head from "next/head";
import Link from "next/link";
import styles from "../styles/Home.module.css";

export default function Home() {
    return (
        <>
            <Head>
                <title>Next Blog | Home</title>
                <meta name="keywords" content="blogs"/>
            </Head>
            <div>
                <h1 className={styles.title}>Homepage</h1>
                <p className={styles.text}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea atque quidem ex delectus nisi facilis libero provident sequi distinctio voluptatem, officiis, tempore praesentium assumenda at ducimus! Unde totam, nihil iste perferendis sunt incidunt ratione sequi animi maxime nisi! Illo error aut aliquam reprehenderit eveniet, consectetur eligendi commodi ad deserunt numquam!</p>
                <p className={styles.text}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea atque quidem ex delectus nisi facilis libero provident sequi distinctio voluptatem, officiis, tempore praesentium assumenda at ducimus! Unde totam, nihil iste perferendis sunt incidunt ratione sequi animi maxime nisi! Illo error aut aliquam reprehenderit eveniet, consectetur eligendi commodi ad deserunt numquam!</p>
                <Link rel="stylesheet" href="/blogs/" className={styles.btn}>
                    see more
                </Link> 
            </div>
        </>
    )
}