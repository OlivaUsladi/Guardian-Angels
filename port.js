const playIcons = document.querySelectorAll(".play-icon");

playIcons.forEach((icon) => {
  icon.addEventListener("click", () => {
    const dataTable = icon.parentNode.querySelector(".data-table");
    if (dataTable.style.display === "none") {
      dataTable.style.display = "table";
    } else {
      dataTable.style.display = "none";
    }
  });
});