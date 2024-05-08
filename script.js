// JavaScript Code
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('uploadButton').addEventListener('click', function() {
      var fileInput = document.getElementById('fileInput');
      var file = fileInput.files[0];
      var formData = new FormData();
      formData.append('file', file);
  
      // Replace '/upload' with the endpoint of your Python compression service
      fetch('/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => response.blob())
      .then(compressedFile => {
        // Handle the compressed file, e.g., download it or display a message

        var url = window.URL.createObjectURL(compressedFile);
            
        // Create a temporary link element
        var link = document.createElement('a');
        link.href = url;
        link.download = 'client_info.docx'; // Specify the filename
        
        // Append the link to the document body
        document.body.appendChild(link);
        
        // Trigger a click event on the link to prompt download
        link.click();
        
        // Clean up
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
        
        console.log('File converted successfully.');
      })
      .catch(error => {
        console.error('Error converting the file:', error);
      });
    });
  });