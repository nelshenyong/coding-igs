async function getTickets() {
    const res = await fetch('https://jsonplaceholder.typicode.com/todos', {
        next: {
            revalidate: 0,
        },
    });

    return res.json();
}

export default async function TicketList() {
    const tickets = await getTickets();

    return (
        <>
            <h1>Tickets</h1>
            {tickets.map(ticket => (
                <div key={ticket.id} className="card mt-5">
                    <h3>{ticket.title}</h3>
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                        Qui, laudantium. Voluptates reprehenderit tempora dolore minus 
                        enim laborum, architecto nisi culpa repellendus quasi ducimus 
                        iure numquam veritatis. Voluptatum, aliquam! Natus, sed?
                    </p>
                    <div className={`pill ${ticket.completed ? 'completed' : 'pending'}`}>
                        {ticket.completed ? 'Completed' : 'Pending'}
                    </div>
                </div>
            ))}
            {tickets.length === 0 && (
                <p className="text-center">
                    There are no open tickets, yay!
                </p>
            )}
        </>
    );
}
