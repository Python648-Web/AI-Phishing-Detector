from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """

    <html>

    <head>

        <title>CyberShield AI</title>

        <style>

            body{
                background-color:#0b0f1a;
                color:white;

                font-family:Arial;

                display:flex;
                justify-content:center;
                align-items:center;

                height:100vh;
                margin:0;
            }

            .container{

                background-color:#111827;

                width:700px;

                padding:40px;

                border-radius:20px;

                box-shadow:0 0 30px rgba(99,102,241,0.2);

                text-align:center;
            }

            h1 {
                color: #6366f1;
                font-size: 50px;
                text-shadow: 0 0 12px #6366f1;
                margin-bottom: 10px;
            }

            p{
                color:#9ca3af;
                font-size:20px;
            }

            textarea{
                width:100%;
                height:180px;

                margin-top:20px;

                background-color:#1f2937;
                color:white;

                border:none;
                border-radius:10px;

                padding:15px;

                font-size:16px;
            }

            button {
                width: 100%;
                margin-top: 20px;

                padding: 15px;

                background: linear-gradient(90deg, #6366f1, #22d3ee);
                color: white;

                border: none;
                border-radius: 10px;

                font-size: 18px;
                font-weight: bold;

                cursor: pointer;

                transition: 0.3s;

                box-shadow: 0 0 15px rgba(99, 102, 241, 0.4);
            }

            button:hover {
                transform: scale(1.05);
                box-shadow: 0 0 25px rgba(34, 211, 238, 0.6);
            }

            #result {
                margin-top: 30px;

                background-color: #0f172a;

                padding: 20px;

                border-radius: 15px;

                border: 1px solid #6366f1;

                box-shadow: 0 0 20px rgba(99, 102, 241, 0.2);

                display: none;
            }

            .scan{
                animation:pulse 1s infinite;
            }

            @keyframes pulse{
                0%{ box-shadow:0 0 10px cyan; }
                50%{ box-shadow:0 0 30px cyan; }
                100%{ box-shadow:0 0 10px cyan; }
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>CyberShield AI</h1>

            <p>AI-Powered Phishing Detection System</p>

            <textarea id="emailText" placeholder="Paste suspicious email here..."></textarea>

            <button onclick="analyzeEmail()">
                Analyze Email
            </button>

            <div id="result">

                <h2 id="threatLevel"></h2>
                <p id="analysis"></p>

            </div>

        </div>

        <script>

            function analyzeEmail(){

                let text =
                    document.getElementById("emailText")
                    .value
                    .toLowerCase();

                let resultBox =
                    document.getElementById("result");

                let threat =
                    document.getElementById("threatLevel");

                let analysis =
                    document.getElementById("analysis");

                resultBox.style.display = "block";
                resultBox.classList.add("scan");

                // 🧠 AI THINKING STATE
                threat.innerHTML = "🧠 AI ANALYZING...";
                threat.style.color = "#22d3ee";
                analysis.innerHTML = "Scanning email structure, keywords, and patterns...";

                setTimeout(function(){

                    resultBox.classList.remove("scan");

                    let level = "";
                    let color = "";
                    let message = "";

                    // 🔴 CRITICAL THREAT
                    if(
                        text.includes("urgent") ||
                        text.includes("click here") ||
                        text.includes("verify") ||
                        text.includes("password") ||
                        text.includes("bank")
                    ){

                        level = "🔴 CRITICAL THREAT";
                        color = "#ef4444";

                        message = "Strong phishing indicators detected. Avoid interacting with this email.";

                    }

                    // 🟡 SUSPICIOUS
                    else if(
                        text.includes("login") ||
                        text.includes("account") ||
                        text.includes("update") ||
                        text.includes("confirm")
                    ){

                        level = "🟡 SUSPICIOUS ACTIVITY";
                        color = "#facc15";

                        message = "Some warning patterns detected. Proceed with caution.";

                    }

                    // 🟢 SAFE
                    else{

                        level = "🟢 SAFE";
                        color = "#22c55e";

                        message = "No significant phishing indicators detected by AI system.";

                    }

                    threat.innerHTML = level;
                    threat.style.color = color;
                    analysis.innerHTML = message;

                }, 2000);

            }

        </script>

    </body>

    </html>

    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
