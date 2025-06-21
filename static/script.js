// paste from clipboard
document.getElementById("paste-btn").addEventListener("click", async () => {
  try {
    const text = await navigator.clipboard.readText();
    document.getElementById("input-text").value = text;
  } catch (err) {
    alert("ไม่สามารถวางข้อความจากคลิปบอร์ดได้");
  }
});

// copy to clipboard
document.getElementById("copy-btn").addEventListener("click", async () => {
  try {
    const output = document.getElementById("translation-output").innerText;
    await navigator.clipboard.writeText(output);
    alert("คัดลอกแล้ว");
  } catch (err) {
    alert("ไม่สามารถคัดลอกข้อความได้");
  }
});

// auto expand textarea
const inputText = document.getElementById("input-text");
inputText.addEventListener("input", () => {
  inputText.style.height = "auto";
  inputText.style.height = inputText.scrollHeight + "px";
});
window.addEventListener("DOMContentLoaded", () => {
  inputText.style.height = "auto";
  inputText.style.height = inputText.scrollHeight + "px";
});

// clear input
document.getElementById("clear-btn").addEventListener("click", () => {
  document.getElementById("input-text").value = "";
  document.getElementById("translation-output").innerText = "";
  inputText.style.height = "auto";
});

// translate
document.getElementById("translate-btn").addEventListener("click", async () => {
  const text = document.getElementById("input-text").value.trim();
  const sourceLang = document.getElementById("source-lang").value;
  const targetLang = document.getElementById("target-lang").value;

  if (!text) {
    alert("กรุณาใส่ข้อความก่อนแปล");
    return;
  }

  try {
    const response = await fetch("/api/translator", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text, source: sourceLang, target: targetLang }),
    });

    const data = await response.json();
    document.getElementById("translation-output").innerText =
      data.translated_text || "ไม่สามารถแปลข้อความได้";
  } catch (err) {
    console.error(err);
    document.getElementById("translation-output").innerText =
      "ไม่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ได้";
  }
});
