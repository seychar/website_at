document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const resultDiv = document.querySelector(".result");

    form.addEventListener("submit", (event) => {
        event.preventDefault(); // Mencegah form di-submit secara default

        // Ambil nilai dari input form
        const sistolik = parseInt(document.getElementById("sistolik").value);
        const diastolik = parseInt(document.getElementById("diastolik").value);
        const age = parseInt(document.getElementById("age").value);
        const gender = document.getElementById("gender").value;
        const lifestyle = document.getElementById("lifestyle").value;
        const diet = document.getElementById("diet").value;
        const physicalActivity = document.getElementById("physical_activity").value;
        const familyHistory = document.getElementById("family_history").value;

        // Fungsi untuk menentukan klasifikasi tekanan darah
        const classifyBloodPressure = (sistolik, diastolik) => {
            if (sistolik < 120 && diastolik < 80) {
                return "Normal";
            } else if ((sistolik >= 120 && sistolik <= 129) && diastolik < 80) {
                return "Elevasi";
            } else if ((sistolik >= 130 && sistolik <= 139) || (diastolik >= 80 && diastolik <= 89)) {
                return "Hipertensi Tahap 1";
            } else if (sistolik >= 140 || diastolik >= 90) {
                return "Hipertensi Tahap 2";
            } else {
                return "Krisis Hipertensi (Segera konsultasi dengan dokter)";
            }
        };

        // Tentukan hasil klasifikasi
        const bloodPressureResult = classifyBloodPressure(sistolik, diastolik);

        // Tentukan solusi atau rekomendasi
        let solusi = "";
        if (bloodPressureResult === "Normal") {
            solusi = "Pertahankan pola hidup sehat Anda.";
        } else if (bloodPressureResult === "Elevasi") {
            solusi = "Mulailah menjaga pola makan dan aktivitas fisik untuk mencegah hipertensi.";
        } else if (bloodPressureResult.includes("Hipertensi")) {
            solusi = "Konsultasikan dengan dokter untuk penanganan lebih lanjut. Perhatikan gaya hidup dan hindari makanan tinggi garam.";
        } else {
            solusi = "Segera cari bantuan medis darurat.";
        }

        // Modifikasi solusi berdasarkan faktor risiko tambahan
        if (familyHistory === "yes" || lifestyle === "poor" || diet === "poor" || physicalActivity === "low") {
            solusi += " Anda memiliki faktor risiko tambahan, jadi sangat disarankan untuk lebih berhati-hati.";
        }

        // Tampilkan hasil dan solusi
        resultDiv.innerHTML = `
            <strong>Hasil: ${bloodPressureResult}</strong>
            <p>${solusi}</p>
        `;
        resultDiv.style.display = "block";
    });
});
