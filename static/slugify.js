const inputTitle = document.querySelector('input[name=title]');
const inputSlug = document.querySelector('input[name=slug]');

const slugify = (val) =>{
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g, '-')  //replacing non word chars, spaces and dashes with single dash
};

inputTitle.addEventListener('keyup', (e) => {
    inputSlug.setAttribute('value', slugify(inputTitle.value));
});
