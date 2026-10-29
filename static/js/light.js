const htmlElement = document.querySelector("html")
const btn = document.querySelector("#btn-theme")


btn.addEventListener("click", () => {
    htmlElement.classList.toggle("light")
})