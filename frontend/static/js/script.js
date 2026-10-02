async function submitPlanner(formId, endpoint) {
    const form = document.getElementById(formId);
    if (!form) return;
    form.addEventListener("submit", async function(event) {
        event.preventDefault();
        const result = document.getElementById("result");
        result.innerHTML = "<div class='result-card'><p>Generating recommendations...</p></div>";
        try {
            const response = await fetch(endpoint, {
                method: "POST",
                body: new FormData(form)
            });
            const data = await response.json();
            let text = String(data.recommendations || "No recommendations found.");
            text = text
                .replace(/PocketSmart AI Recommendations/gi, "")
                .replace(/Approx\./gi, "")
                .replace(/\?/g, "Rs.")
                .replace(/\*\*/g, "")
                .replace(/###/g, "")
                .replace(/---/g, "")
                .replace(/\\n/g, " ")
                .replace(/\s+/g, " ")
                .trim();
            result.innerHTML =
                "<div class='result-card'>" +
                "<h2>PocketSmart AI Recommendations</h2>" +
                "<p>" + text + "</p>" +
                "</div>";
        } catch (error) {
            result.innerHTML =
                "<div class='result-card'>" +
                "<h2>Something went wrong</h2>" +
                "<p>Please check the server and try again.</p>" +
                "</div>";
        }
    });
}
