const likeButton = document.querySelector('.like-button');
const likeCount = document.querySelector('.like-count');

likeButton.addEventListener('click', () => {
    const currentCount = parseInt(likeCount.textContent, 10);
    likeCount.textContent = currentCount +1;
})