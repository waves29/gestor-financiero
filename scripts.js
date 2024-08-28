// Función para agregar un ingreso a la lista
function addIngreso() {
    // Obtener valores del formulario de ingreso
    const monto = document.getElementById('ingreso-monto').value;
    const descripcion = document.getElementById('ingreso-descripcion').value;

    // Validar entrada
    if (monto === '' || descripcion === '') {
        alert('Por favor, complete todos los campos.');
        return;
    }

    // Crear un nuevo elemento de lista para el ingreso
    const listItem = document.createElement('li');
    listItem.textContent = `$${parseFloat(monto).toFixed(2)} - ${descripcion}`;
    
    // Agregar el nuevo elemento a la lista
    document.getElementById('ingreso-list').appendChild(listItem);

    // Limpiar los campos del formulario
    document.getElementById('ingreso-form').reset();
}

// Función para agregar un gasto a la lista
function addGasto() {
    // Obtener valores del formulario de gasto
    const monto = document.getElementById('gasto-monto').value;
    const descripcion = document.getElementById('gasto-descripcion').value;

    // Validar entrada
    if (monto === '' || descripcion === '') {
        alert('Por favor, complete todos los campos.');
        return;
    }

    // Crear un nuevo elemento de lista para el gasto
    const listItem = document.createElement('li');
    listItem.textContent = `$${parseFloat(monto).toFixed(2)} - ${descripcion}`;
    
    // Agregar el nuevo elemento a la lista
    document.getElementById('gasto-list').appendChild(listItem);

    // Limpiar los campos del formulario
    document.getElementById('gasto-form').reset();
}

// Función para calcular el balance mensual
function calcularBalance() {
    // Obtener los elementos de la lista de ingresos y gastos
    const ingresosList = document.getElementById('ingreso-list').getElementsByTagName('li');
    const gastosList = document.getElementById('gasto-list').getElementsByTagName('li');

    let totalIngresos = 0;
    let totalGastos = 0;

    // Sumar los ingresos
    for (let item of ingresosList) {
        const monto = parseFloat(item.textContent.split(' - ')[0].replace('$', ''));
        totalIngresos += monto;
    }

    // Sumar los gastos
    for (let item of gastosList) {
        const monto = parseFloat(item.textContent.split(' - ')[0].replace('$', ''));
        totalGastos += monto;
    }

    // Calcular el balance
    const balance = totalIngresos - totalGastos;

    // Mostrar el resultado en el elemento de balance
    document.getElementById('balance-result').textContent = `Balance Mensual: $${balance.toFixed(2)}`;
}
