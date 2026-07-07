// =========================
// Start Learning Button
// =========================

function showMessage() {
    window.location.href = "/bell";
}


// =========================
// Card Animation
// =========================

const cards = document.querySelectorAll(".card");

cards.forEach((card) => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-12px) scale(1.03)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px) scale(1)";

    });

});


// =========================
// Smooth Fade Animation
// =========================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});


// =========================
// Create Floating Particles
// =========================

function createParticle() {

    const particle = document.createElement("span");

    particle.classList.add("particle");

    particle.style.left = Math.random() * window.innerWidth + "px";

    particle.style.animationDuration = (4 + Math.random() * 6) + "s";

    particle.style.opacity = Math.random();

    particle.style.width = particle.style.height =
        (4 + Math.random() * 8) + "px";

    document.body.appendChild(particle);

    setTimeout(() => {

        particle.remove();

    }, 10000);

}

setInterval(createParticle, 250);