function checkFraud() {
    let text = document.getElementById("inputText").value;

    fetch("https://sms-detector.onrender.com/check", {  // ✅ Use live backend
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })  // ✅ Sending JSON data
    })
    .then(response => response.json())
    .then(data => { 
        document.getElementById("result").innerText = data.result; 
    })
    .catch(error => console.error("Error:", error));
}
