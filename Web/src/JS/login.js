// Asegúrate que este código esté en /Web/src/JS/login.js

// ----------------------------------------------------
// 1. Función para establecer el Rol y dar feedback visual
// ----------------------------------------------------
function setRole(role, event) {
    document.getElementById("role").value = role;
    document.getElementById("roleDisplay").textContent = `Selected Role: ${role}`;
    
    document.querySelectorAll("button[onclick^='setRole']").forEach(btn => {
        btn.classList.remove("btn-warning");
    });
    
    if (event && event.target) {
        // Asume que el botón Cliente ya tiene btn-warning por defecto en el HTML,
        // por eso lo añadimos aquí a los demás para que se mantenga el color.
        event.target.classList.add("btn-warning");
    }
}

// ----------------------------------------------------
// 2. Función principal para el Login (Se activa al enviar el formulario)
// ----------------------------------------------------
async function loginUser(event) {
    event.preventDefault(); 

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    if (!role) {
        alert("Por favor, selecciona un rol antes de ingresar.");
        return;
    }

    try {
        // Apuntamos al puerto 8000 (Python/FastAPI)
        const response = await fetch("http://localhost:8000/login", { 
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password, role }),
        });
    
        // Manejo del error 401 de FastAPI
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail.message || "Error en las credenciales");
        }

        const data = await response.json();

        if (data.success) {
            alert(`¡Ingreso exitoso! ${data.message}`);

            // Usamos la URL de redirección enviada por el Backend
            if (data.redirectUrl) {
                window.location.href = data.redirectUrl;
            } else {
                window.location.href = "/index.html"; 
            }
        } else {
            alert(data.message || "Error al iniciar sesión.");
        }

    } catch (error) {
        console.error("Error al conectar con el servidor:", error);
        alert(error.message); 
    }
}
