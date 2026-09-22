const uploadForm = document.getElementById("uploadForm");

const fileInput = document.getElementById("architectureFile");

const reviewButton = document.getElementById("reviewButton");

const statusMessage = document.getElementById("statusMessage");

const resultsSection = document.getElementById("resultsSection");

const reviewResults = document.getElementById("reviewResults");

const reviewFilename = document.getElementById("reviewFilename");


uploadForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const file = fileInput.files[0];

    if (!file) {
        statusMessage.textContent = "Please select a Markdown file.";
        return;
    }

    // Clear previous results
    reviewResults.replaceChildren();

    resultsSection.hidden = true;

    statusMessage.textContent = "Analyzing your architecture...";

    reviewButton.disabled = true;

    // Prepare the uploaded file
    const formData = new FormData();

    formData.append("file", file);

    try {

        // Send the file to FastAPI
        const response = await fetch("/review", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        // Handle unsuccessful responses
        if (!response.ok) {

            throw new Error(
                typeof data.detail === "string"
                    ? data.detail
                    : "Something went wrong while reviewing the architecture."
            );

        }

        // Extract the generated review
        const pros = data.review.pros;

        const cons = data.review.cons;

        // Find the number of rows needed
        const rowCount = Math.max(pros.length, cons.length);

        // Create table rows
        for (let i = 0; i < rowCount; i++) {

            const row = document.createElement("tr");

            const proCell = document.createElement("td");

            const conCell = document.createElement("td");

            proCell.textContent = pros[i] || "";

            conCell.textContent = cons[i] || "";

            row.appendChild(proCell);

            row.appendChild(conCell);

            reviewResults.appendChild(row);

        }

        reviewFilename.textContent = `File: ${data.filename}`;

        resultsSection.hidden = false;

        statusMessage.textContent = "Architecture review completed!";

    } catch (error) {

        statusMessage.textContent = error.message;

    } finally {

        reviewButton.disabled = false;

    }

});