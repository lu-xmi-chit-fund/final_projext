navbar_1=document.getElementById("navbar_1")
console.log(navbar_1)
top_offset=navbar_1.offsetTop;

function stickynavbar()
{
    if(window.scrollY>top_offset)
        navbar_1.classList.add('sticky')
    else
        navbar_1.classList.remove('sticky')
}

window.addEventListener('scroll',stickynavbar)
