function edit(id) {
    let edit_review = document.querySelector(`#edit-review-${id}`);
    let edit_btn = document.querySelector(`#edit-btn-${id}`);
    edit_review.style.display = 'block';
    edit_btn.style.display = 'block';

    edit_btn.addEventListener('click', () => {
        fetch('/edit/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                review: edit_review.value
            })
          });
          edit_review.style.display = 'none';
          edit_btn.style.display = 'none';
          document.querySelector(`#review-${id}`).innerHTML = edit_review.value;
    });
    edit_review.value = "";
    return false;
}


