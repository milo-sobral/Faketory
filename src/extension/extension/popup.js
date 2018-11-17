/*document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');
  checkPageButton.addEventListener('click', function() {

    chrome.tabs.getSelected(null, function(tab) {
      d = document;

      var f = d.createElement('form');
      f.action = 'http://gtmetrix.com/analyze.html?bm';
      f.method = 'post';
      var i = d.createElement('input');
      i.type = 'hidden';
      i.name = 'url';
      i.value = tab.url;
      f.appendChild(i);
      d.body.appendChild(f);
      f.submit();
    });
  }, false);
}, false);

chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
});

$(document).ready(function ()) {
  chrome.tabs.getSelected(null, function (tab) {
    var link = document.createElement('a');

  })
};


chrome.tabs.query({'active': true, 'lastFocusedWindow': true, 'currentWindow': true}, function (tabs) {
    var url = tabs[0].url;
    console.log(url);
});

*/

// Our hash
var tabIdToURL = {};
var currentTabId = -1;
// Add changes to the hash (tab creation, tab's page load)
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    tabIdToURL[tabId] = tab.url; // also available as tab.id and changeInfo.url
});
// Remove entries from closed tabs
chrome.tabs.onRemoved.addListener(function(tabId) {
    delete tabIdToURL[tabId];
});
// Set the ID of the current active tab
chrome.tabs.onActivated.addListener(function(activeInfo) {
    currentTabId = activeInfo.tabId;
});

// Usage, based on the question's function
function getURL() {
    return tabIdToURL[currentTabId];
}
