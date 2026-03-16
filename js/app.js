const getCurrentYear = (() => {    
    let year = new Date().getFullYear()
    let footer = document.querySelector("footer")
    footer.append(year)
})()
