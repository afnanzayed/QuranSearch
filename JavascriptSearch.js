async function searchVerse() {
  const query = document.getElementById("query").value; // Get search word
  const resultsList = document.getElementById("resultsList");
  resultsList.innerHTML = ""; // Dump previous results

  try {
      // Send request to server
      const response = await fetch(`http://127.0.0.1:5000/search?query=${query}`);
      if (!response.ok) {
          const errorMessage = await response.text();
          throw new Error(`Error fetching data: ${errorMessage}`);
      }

      const data = await response.json();
      console.log("Data received from backend:", data);

      // Results
      if (data.results.length === 0) {
          const li = document.createElement("li");
          li.textContent = "No results found.";
          resultsList.appendChild(li);
      } else {
          data.results.forEach((result) => {
              const li = document.createElement("li");
              li.innerHTML = `
                  <strong>Surah:</strong> ${result.surah}<br>
                  <strong>Revelation Type:</strong> ${result.revelationType}<br>
                  <strong>Ayah Number:</strong> ${result.ayah}<br>
                  <strong>Text:</strong> ${result.text}
              `;
              resultsList.appendChild(li);
          });
      }
  } catch (error) {
      console.error("Error:", error);
      const li = document.createElement("li");
      li.textContent = `An error occurred: ${error.message}`;
      resultsList.appendChild(li);
  }
}
