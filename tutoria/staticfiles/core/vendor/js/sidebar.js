const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('mainContent');
const toggleSidebar = document.getElementById('toggleSidebar');
const accordionTutor = document.getElementById('collapseTutor');

toggleSidebar.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
    mainContent.classList.toggle('collapsed');

    // Si el sidebar se colapsa, cerramos el acordeón del tutor
    if (sidebar.classList.contains('collapsed')) {
        // Asegúrate de que Bootstrap esté cargado y funcionando
        const collapseInstance = bootstrap.Collapse.getOrCreateInstance(accordionTutor);
        collapseInstance.hide();
    }
});
