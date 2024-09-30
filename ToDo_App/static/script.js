 // JavaScript to display message
 const deleteConfirmModal = document.getElementById('deleteConfirmModal');
 deleteConfirmModal.addEventListener('show.bs.modal', function (event) {
     const button = event.relatedTarget;
     const taskId = button.getAttribute('data-taskid');
     const deleteForm = document.getElementById('deleteTaskForm');
     deleteForm.action = `/todo/delete/${taskId}/`;
 });

 // Dark Mode Toggle 
 const html = document.getElementById("htmlPage");
 const checkbox = document.getElementById('checkbox');
 checkbox.addEventListener("change", () => {
     if (checkbox.checked) {
         html.setAttribute("data-bs-theme", "dark");
     } else {
         html.setAttribute("data-bs-theme", "light");
     }
 });