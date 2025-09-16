async function mostrarSesiones(page = 1, size = 5) {
    try {
        const url = `/api/sesiones?page=${page}&size=${size}`;
        const response = await fetch(url); 
        if (!response.ok) throw new Error(`Error en la petición ${response.status}`);

        const data = await response.json();

        // Llenar tabla
        const tabla = document.getElementById("tablaDatos");
        tabla.innerHTML = "";

        data.results.forEach(sesion => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${new Date(sesion.fecha_sesion).toLocaleString()}</td>
                <td>${sesion.motivo_sesion}</td>
                <td>-</td>
                <td>${sesion.estado}</td>
            `;
            tabla.appendChild(fila);
        });

        const contenedor = document.getElementById("paginacion");
        contenedor.innerHTML = `
            <button ${!data.previous ? "disabled" : ""} onclick="mostrarSesiones(${page - 1}, ${size})" class="btn btn-secondary me-2">Anterior</button>
            <button ${!data.next ? "disabled" : ""} onclick="mostrarSesiones(${page + 1}, ${size})" class="btn btn-secondary">Siguiente</button>
        `;

    } catch(error) {
        console.error(error);
    }
}

 document.addEventListener("DOMContentLoaded", () => {
        const sizeSelect = document.getElementById("sizeSelect");

        function getSize() {
            return parseInt(sizeSelect.value);
        }

        // Cargar la primera página
        mostrarSesiones(1, getSize());

        // Cambiar tamaño de página recarga la tabla
        sizeSelect.addEventListener("change", () => mostrarSesiones(1, getSize()));
    });