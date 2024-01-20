chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  chrome.tabs.sendMessage(tabs[0].id, { action: "getLinks" });
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "displayLinks") {
    console.log("Extracted Links:", request.links);
  }
});



function sendLinksToServer(links) {
  const apiUrl = 'http://localhost:8000/receive_links/';
  const data = { links: links };

  fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(result => {
      console.log('Server response:', result);
    })
    .catch(error => {
      console.error('Error sending links to server:', error);
    });
}