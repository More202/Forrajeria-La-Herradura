document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal');
    var openModalBtn = document.getElementById('openModalBtn');
    var closeModalBtn = document.getElementById('closeModalBtn');
    var aperturaCajaForm = document.getElementById('aperturaCajaForm');

    if (openModalBtn) {
        openModalBtn.onclick = function() {
            modal.style.display = "block";
        }
    }

    if (closeModalBtn) {
        closeModalBtn.onclick = function() {
            modal.style.display = "none";
        }
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    if (aperturaCajaForm) {
        aperturaCajaForm.onsubmit = function(e) {
            e.preventDefault();
            var montoInicial = document.getElementById('montoInicial').value;
            if (montoInicial) {
                this.submit();
            } else {
                alert('Por favor, ingrese un monto inicial.');
            }
        }
    }
});