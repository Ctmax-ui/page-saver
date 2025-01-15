const darkThemeToggler = document.getElementById("darkThemeToggler");

localStorage.getItem("pageSaverDarkMode") == ""
  ? ""
  : document.body.classList.add("bg-dark");

darkThemeToggler?.addEventListener("click", () => {
  document.body.classList.toggle("bg-dark");
  if (document.body.classList.contains("bg-dark")) {
    localStorage.setItem("pageSaverDarkMode", "bg-dark");
  } else {
    localStorage.setItem("pageSaverDarkMode", "");
  }
});

var globalFontSize = localStorage.getItem("pageSaverFontSize") || 16;

async function fetchData() {
  const totlaFileName = document.getElementById("total-files");
  const query = document.getElementById("query");
  const res = await fetch("./data/data.json");
  const data = await res.json();
  totlaFileName.innerText = `Total Files : ${data.length}`;
  query.innerText = `Query : none`;
  renderFileList(data);
  document.getElementById("searchInput").addEventListener("input", (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const filteredData = data
      .map((item) => {
        const highlightedItem = { ...item };
        if (searchTerm) {
          highlightedItem.fileName = highlightText(item.fileName, searchTerm);
          highlightedItem.category = highlightText(item.category, searchTerm);
          highlightedItem.timestamp = highlightText(item.timestamp, searchTerm);
        }
        return highlightedItem;
      })
      .filter(
        (item) =>
          item.fileName.toLowerCase().includes(searchTerm) ||
          item.category.toLowerCase().includes(searchTerm) ||
          item.timestamp.toLowerCase().includes(searchTerm)
      );
    renderFileList(filteredData);
    totlaFileName.innerText = `Total Files : ${filteredData.length}`;
    query.innerText = `Query : ${searchTerm || "none"}`;
  });
}

function renderFileList(files) {
  const fileList = document.getElementById("fileList");
  fileList.innerHTML = "";

  if (files.length === 0) {
    fileList.innerHTML =
      '<p class="text-center text-muted">No files found.</p>';
    return;
  }

  files.forEach((file) => {
    const listItem = document.createElement("div");
    listItem.setAttribute("data-href", file.filePath);
    listItem.className =
      "group-list custom-text-white px-3 py-2 d-flex justify-content-between align-items-center gap-3 border border-dark";
    listItem.style.cursor = "pointer";
    listItem.innerHTML = `
            <span class="badge bg-primary rounded-pill">${file.count}</span>
            <div class="w-100">
                <h5 class="mb-3">${file.fileName}</h5>
                <div class="mb-0 d-flex justify-content-between">
                    <p class="m-0"><strong>Category:</strong> <span class="bg-warning rounded-pill px-2">${file.category}</span></p> 
                    <p class="m-0 fw-bold">${file.timestamp}</p>
                </div>
            </div>
        `;
    fileList.appendChild(listItem);
  });

  var prevItem = null;
  document.querySelectorAll(".group-list").forEach((items) => {
    items.addEventListener("click", (e) => {
      e.preventDefault();
      const targetItem = e.target.closest(".group-list");
      if (prevItem == targetItem) {
        return;
      }

      prevItem = targetItem;
      const iframeContainer = document.createElement("div");
      iframeContainer.className =
        "iframe-container position-fixed top-0 start-0 w-100 h-100 z-3 bg-light";
      const iframe = document.createElement("iframe");
      iframe.src = targetItem.dataset.href;
      iframe.className = "w-100 h-100 border-0";

      const sizeBtns = document.createElement("div");
      sizeBtns.className =
        "position-absolute top-0 start-0 mt-2 ms-5 d-flex gap-2";
      const sizeIncrementBtn = document.createElement("button");
      sizeIncrementBtn.textContent = "➕";
      sizeIncrementBtn.className = "btn btn-warning border border-dark";
      sizeIncrementBtn.addEventListener("click", () => {
        const iframeDoc =
          iframe.contentDocument || iframe.contentWindow.document;
        iframeDoc.body.style.fontSize = `${(globalFontSize++)}px`;
        localStorage.setItem("pageSaverFontSize", globalFontSize);
      });
      sizeBtns.appendChild(sizeIncrementBtn);
      const sizeDecrementBtn = document.createElement("button");
      sizeDecrementBtn.textContent = "➖";
      sizeDecrementBtn.className = "btn btn-warning border border-dark";
      sizeDecrementBtn.addEventListener("click", () => {
        const iframeDoc =
          iframe.contentDocument || iframe.contentWindow.document;
        iframeDoc.body.style.fontSize = `${(globalFontSize -= 2)}px`;
        localStorage.setItem("pageSaverFontSize", globalFontSize);
      });
      sizeBtns.appendChild(sizeDecrementBtn);
      iframeContainer.appendChild(sizeBtns);

      const closeButton = document.createElement("button");
      closeButton.textContent = "✖";
      closeButton.className =
        "btn btn-danger position-absolute top-0 end-0 mt-2 me-5";
      closeButton.addEventListener("click", () => {
        document.body.removeChild(iframeContainer);
        prevItem = null;
      });
      iframeContainer.appendChild(iframe);
      iframeContainer.appendChild(closeButton);
      document.body.appendChild(iframeContainer);
    });
  });
}
if (document.getElementsByClassName("text-break")[0]) {
  document.getElementsByClassName(
    "text-break"
  )[0].style.fontSize = `${globalFontSize}px`;
}

function highlightText(text, searchTerm) {
  const regex = new RegExp(`(${searchTerm})`, "gi");
  return text.replace(regex, '<span class="bg-info">$1</span>');
}

fetchData();
