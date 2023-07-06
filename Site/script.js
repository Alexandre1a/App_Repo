fetch('manifest.json')
  .then(response => response.json())
  .then(data => {
    const lastVersion = data.version;
    document.getElementById('last-version').textContent = `Dernière version : ${lastVersion}`;
  })
  .catch(error => {
    console.error('Une erreur s\'est produite lors de la récupération du manifest.json :', error);
  });
