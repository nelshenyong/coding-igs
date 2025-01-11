import Link from "next/link";
import { useEffect } from "react";
import { useRouter } from "next/router";

const NotFound = () => {
    const router = useRouter()

    useEffect(() => {
        setTimeout(() => {
            // router.go(-1)
            // router.go(1)
            router.push("/")
        }, 3000)
    }, [])
    
    return (
        <>
            <h1>404 - Page Not Found</h1>
            <h2>Redirecting to Home Page...</h2>
        </>
    );

    return (
        <div className="not-found">
            <h1>Ooops...</h1>
            <h2>That page cannot be found :(</h2>
            <p>Go back to the clock <Link href="/">Homepage</Link></p>
        </div>
    )
}