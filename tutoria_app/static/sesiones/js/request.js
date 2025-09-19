let sortField = 'id';       
let sortOrder = '';         

async function mostrarSesiones(page = 1, size = 5) {
    try {
        const url = `/api/sesiones?page=${page}&size=${size}&order=${sortOrder}${sortField}`;
        const response = await fetch(url); 
        if (!response.ok) throw new Error(`Error en la petición ${response.status}`);

        const data = await response.json();
        const tabla = document.getElementById("tablaDatos");
        tabla.innerHTML = "";

        data.results.forEach(sesion => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${new Date(sesion.fecha_sesion).toLocaleString()}</td>
                <td>${sesion.motivo_sesion}</td>
                <td>${sesion.estado}</td>
                <td>${sesion.detalles || '-'}</td>
            `;
            tabla.appendChild(fila);
        });

        const contenedor = document.getElementById("paginacion");
        contenedor.innerHTML = `
            <button ${!data.previous ? "disabled" : ""} onclick="mostrarSesiones(${page - 1}, ${size})" class="btn btn-outline-primary me-2">Anterior</button>
            <button ${!data.next ? "disabled" : ""} onclick="mostrarSesiones(${page + 1}, ${size})" class="btn btn-outline-primary">Siguiente</button>
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

    mostrarSesiones(1, getSize());

    sizeSelect.addEventListener("change", () => mostrarSesiones(1, getSize()));

    document.querySelectorAll('th').forEach(th => {
        th.style.cursor = 'pointer';
        th.addEventListener('click', () => {
            const campo = th.textContent.trim(); // Obtener nombre de columna
            const map = {
                'fecha sesión': 'fecha_sesion',
                'motivo sesión': 'motivo_sesion',
                'detalles': 'detalles',
                'status': 'estado'
            };
            if (sortField === map[campo]) {
                sortOrder = sortOrder === '' ? '-' : '';
            } else {
                sortField = map[campo];
                sortOrder = '';
            }
            mostrarSesiones(1, getSize());
        });
    });
});
