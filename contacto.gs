// Google Apps Script — cami.clipp Brief Form → Google Sheets
// INSTRUCCIONES:
// 1. Abrí scripts.google.com → Nuevo proyecto
// 2. Pegá este código completo
// 3. Guardá (Ctrl+S)
// 4. Clic en "Implementar" → "Nueva implementación"
// 5. Tipo: Aplicación web
// 6. Ejecutar como: Yo (tu cuenta Google)
// 7. Quién tiene acceso: Cualquier usuario
// 8. Copiá la URL que te da y pegala en index.html donde dice PEGAR_URL_APPS_SCRIPT_AQUI

const SHEET_ID = 'PEGAR_ID_DE_TU_GOOGLE_SHEET'; // El ID está en la URL de tu Sheet

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.openById(SHEET_ID).getActiveSheet();
    const data = JSON.parse(e.postData.contents);

    // Si la sheet está vacía, agrega encabezados
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        'Fecha', 'Nombre', 'WhatsApp', 'Email',
        'Instagram', 'Rubro', 'Plan', 'Mensaje'
      ]);
      sheet.getRange(1, 1, 1, 8).setFontWeight('bold');
    }

    sheet.appendRow([
      data.fecha || new Date().toLocaleString('es-AR'),
      data.nombre || '',
      data.whatsapp || '',
      data.email || '',
      data.instagram || '',
      data.rubro || '',
      data.plan || '',
      data.mensaje || ''
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({status: 'ok'}))
      .setMimeType(ContentService.MimeType.JSON);

  } catch(err) {
    return ContentService
      .createTextOutput(JSON.stringify({status: 'error', message: err.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService.createTextOutput('cami.clipp brief form — OK');
}
