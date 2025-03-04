function checkFraud() {
    let text = document.getElementById("inputText").value;

    fetch("http://127.0.0.1:5000/check", {  // ✅ Correct URL
        method: "POST",                      // ✅ Using POST request
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }) // ✅ Sending JSON data
    })
    .then(response => response.json())
    .then(data => { 
        document.getElementById("result").innerText = data.result; 
    })
    .catch(error => console.error("Error:", error));
}
