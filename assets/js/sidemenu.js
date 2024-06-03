window.dash_clientside = Object.assign({}, window.dash_clientside, {
  sidemenu: {
    create_events: function (a) {
      let sidebarCollapsed, sidebarExpanded;
      let content_found = setInterval(waitForContentLoad, 1000);
      function waitForContentLoad() {
        let main_content = document.getElementById("_pages_content");
        if (main_content !== null) {
          clearInterval(content_found);
        }
      }
      sidebarCollapsed = document.getElementById("side-menu-collapsed");
      sidebarExpanded = document.getElementById("side-menu-expanded");
      sidebarCollapsed.addEventListener("mousemove", (e) => {
        sidebarCollapsed.style.display = "none";
        sidebarExpanded.style.display = "block";
      });

      sidebarExpanded.addEventListener("mouseleave", function (event) {
        sidebarCollapsed.style.display = "block";
        sidebarExpanded.style.display = "none";
      });
      return window.dash_clientside.no_update;
    },
  },
});
