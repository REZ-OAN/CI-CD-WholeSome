// Use the service name instead of localhost
const API_URL = window.location.hostname === "localhost"
  ? "http://localhost:3030/api/data" // For browser access
  : "http://backend:3030/api/data";  // For internal Docker communication

async function fetchData() {
    try {
        // Add error handling and logging
        const response = await fetch(API_URL, {
            method: 'GET',
            headers: { 
                'Content-Type': 'application/json',
                // Add additional headers for CORS
                'Access-Control-Allow-Origin': '*'
            }
        });

        // Check if the response is ok
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        const list = document.getElementById('data-list');
        list.innerHTML = '';
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item.name;
            list.appendChild(li);
        });
    } catch (error) {
        console.error('Fetch data error:', error);
        // Optionally, show error to user
        alert(`Failed to fetch data: ${error.message}`);
    }
}

async function addData() {
    try {
        const newData = document.getElementById('new-data').value;
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                // Add additional headers for CORS
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({ data: newData })
        });

        // Check if the response is ok
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        document.getElementById('new-data').value = '';
        await fetchData();
    } catch (error) {
        console.error('Add data error:', error);
        // Optionally, show error to user
        alert(`Failed to add data: ${error.message}`);
    }
}

// Call fetchData when the page loads
fetchData();