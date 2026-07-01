#include "app-window.h"
#include "webview-ext.h"

int main(int argc, char **argv)
{
    auto ui = App::create();

    ui->set_window_title("SurrealTree Explorer v1.0");

    std::unique_ptr<webview::webview> wv = nullptr;

    ui->on_menu_changed([&](int index, slint::SharedString page_ix, slint::SharedString page_name) {
        // Converts perfectly now!
        std::string converted_id = page_ix.data();
        std::cout << "Menu changed! Index: " << index << ", ID: " << converted_id << std::endl;

        if (index == 0) {
        } else if (index == 1) {
            // show_and_align_webview(ui.operator->(), wv, "https://github.com/odys-z");
            launch_webview_window(ui);
        } else if (index == 2) {
        } else {
        }
    });

    ui->run();
    return 0;
}
