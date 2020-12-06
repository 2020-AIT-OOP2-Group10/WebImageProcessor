if (files.length > 0) {

    // <p>の親要素<div>
    const div = document.getElementById("img_list");

    for (let i=0; i<files.length; i++) {
        
        // <img>の親要素<p>
        let p = document.createElement("p");
        div.appendChild(p);

        // <img>
        let img = document.createElement("img");
        img.src = files[i];
        img.alt = files[i];

        p.appendChild(img);

    }

}