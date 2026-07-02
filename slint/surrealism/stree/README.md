# About

  The HelloWorld of SurrealismUI.

# Walk Through

1. Start from Sources

    See SurrealismUI/tests for latest version.

    Download code zip, extract to, say, surrealism-ui-nightly.

    Config .vscode/settings.json & CMakeLists.txt.

    ```
      {
        "slint.libraryPaths": {
            "surrealism": "../surrealism-ui-nightly"
        }
      }
    ```
    ```
      get_filename_component(SURREALISM_UI_DIR 
        "${CMAKE_CURRENT_SOURCE_DIR}/../surrealism-ui-nightly" 
        ABSOLUTE
      )
    ```

1. Compile with MinGW + GCC 16.1.0

    ```
      export PATH="/c/Qt-6.10/Tools/CMake_64/bin:$PATH"
      export PATH="/c/Qt-6.10/mingw64-gcc16.1.0/bin:$PATH"
      rustup target add --toolchain stable-x86_64-pc-windows-msvc x86_64-pc-windows-gnu
      # WIN32 for the first time or any fetch contents updata
      cmake -G "MinGW Makefiles" -B build -DFETCHCONTENT_BASE_DIR="C:/CMakeCache" -DFETCHCONTENT_FULLY_DISCONNECTED=FALSE
      # to avoid github downloading
      cmake -G "MinGW Makefiles" -B build -DFETCHCONTENT_BASE_DIR="C:/CMakeCache" -DFETCHCONTENT_FULLY_DISCONNECTED=ON
      cmake --build build
      build/my_application.exe
    ```

1. Switching Function Pages

    ```
      menu:=SMenu {
        change(index, data) => {
          debug(index, data);
          router-index = index;
          menu-changed(index, data.id, data.name);
        }
      }

      right-wrapper:=Rectangle {
        if router-index==0: index-page:= Rectangle {
        }
        if router-index==1: index-page:= Rectangle {
        }
      }
    ```

1. Embed a WebView

    Currently Slint cannot embed a product ready webview window. That's not released.

    To popup a separate window,

    ```
      webview::webview w(true, nullptr);
      w.set_title("Popup Webview");
      w.set_size(600, 500, WEBVIEW_HINT_NONE);
      
      // The script run at onload().
      w.init("window.addEventListener('DOMContentLoaded', () => { if(typeof foo === 'function') foo(); });");

      w.navigate("https://github.com/webview/webview");
    ```

    The Webview can fully support ReactJS pages.

1. Implement a Filesystem Explorer

    - The failed experiment

    SurrealismUI provide a tree view component, STree. But it fails compile. According to Gemini, it will trigger a
    slint compiler's bug in its ScrolView.

    ```
      auto FilesystemExplorer_root_32::init (const class SharedGlobals* globals,
            slint::cbindgen_private::ItemTreeWeak enclosing_component,
            uint32_t tree_index, uint32_t tree_index_of_first_child) -> void{

        return ((tmp_root_32_horizontal_bar_79_maximum <= (0 /(float) self->globals->window().window_handle().scale_factor()) ? 0 :
          [&]{ [[maybe_unused]] auto tmp_root_32_horizontal_bar_79_page_size = self->field_root_32_children_view_49_visible_width.get();;
            return (std::max<float>(std::min<float>(16,

                // THIS IS INVALID C++ CODE
                if (self->field_root_32_vertical_bar_66_visible.get()) { (100 -(float) 14); } else { 100; }), 

                ...);
            }();
        ...
    ```

    Uncomment the line in app-window.slint to reproduce the error.

    ```
      FilesystemExplorer { width: 100%; height: 100%; }
    ```

    - The Treeview solution

    Use a flat table with leading cells representing indentions. See ui/custom-table.sling.

    ```
      property <[CustomRowData]> custom_rows: [
        { has_icon: true,
          icons: [@image-url("imgs/add.svg"), @image-url("imgs/dash.svg")], // <-- Indentions
          text_col1: "Item 1.2", text_col2: "Item 1.3" },
        { has_icon: false, icons: [], text_col1: "Item 2.2", text_col2: "Item 2.3" },
      ];

      HorizontalLayout {
        width: 30%;
        spacing: 8px;

        // render the cell
        for icon in row.icons : Image {
            source: icon;
            width: 32px;
            height: 32px;
        }
        if (!row.has_icon) : Text {
            text: row.text_col1;
        }
      }
    ```
