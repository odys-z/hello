#pragma once
#include <filesystem>
#include <unordered_map>
#include <memory>

#include "app-window.h"
#include "file-tree.h"

namespace fs = std::filesystem;

class FilesystemPage {
public:
    explicit FilesystemPage(App* ui_instance) : ui(ui_instance) {}

    void init_view() {
        fs::path current_dir = fs::current_path();
        
        TreeData root_node;
        root_node.label = current_dir.filename().string();
        root_node.extra = current_dir.string();
        root_node.is_dir = true;
        root_node.is_expanded = true;
        root_node.children = std::make_shared<slint::VectorModel<TreeItem>>(scan_directory(current_dir));
        
        ui->set_fs_data(root_node);
        bind_ui_events();
    }

private:
    AppWindow* ui;
    std::unordered_map<std::string, std::string> backend_records;

    void bind_ui_events() {
        ui->on_forward_click([this](slint::SharedString path, bool is_dir) {
            TreeItem tree_snapshot = ui->get_fs_data();
            if (process_node(tree_snapshot, path.to_string())) {
                ui->set_fs_data(tree_snapshot);
            }
        });

        ui->on_forward_sync([this]() {
            // Live background service record update
            backend_records[ (fs::current_path() / "data.csv").string() ] = "Bound ID #9411";
            TreeItem tree_snapshot = ui->get_fs_data();
            sync_tree_nodes(tree_snapshot);
            ui->set_fs_data(tree_snapshot);
        });
    }

    slint::Vector<TreeItem> scan_directory(const fs::path& target) {
        slint::Vector<TreeItem> items;
        try {
            for (const auto& entry : fs::directory_iterator(target)) {
                TreeItem item;
                item.label = entry.path().filename().string();
                item.extra = entry.path().string();
                item.is_dir = entry.is_directory();
                item.children = item.is_dir ? std::make_shared<slint::VectorModel<TreeItem>>() : nullptr;
                items.push_back(item);
            }
        } catch (...) {}
        return items;
    }

    bool process_node(TreeItem& node, const std::string& target_path) {
        if (node.extra == target_path) {
            if (node.is_dir) {
                node.is_expanded = !node.is_expanded;
                if (node.is_expanded && (node.children == nullptr || node.children->row_count() == 0)) {
                    node.children = std::make_shared<slint::VectorModel<TreeItem>>(scan_directory(fs::path(target_path)));
                }
            } else if (node.binding_info.empty()) {
                node.selected = !node.selected; // Check rule: selection allowed if unbound
            }
            return true;
        }
        
        if (node.children != nullptr) {
            auto model = std::dynamic_pointer_cast<slint::VectorModel<TreeItem>>(node.children);
            if (model) {
                for (int i = 0; i < model->row_count(); ++i) {
                    TreeItem child = *model->row_data(i);
                    if (process_node(child, target_path)) {
                        model->set_row_data(i, child);
                        return true;
                    }
                }
            }
        }
        return false;
    }

    void sync_tree_nodes(TreeItem& node) {
        std::string p = node.extra.to_string();
        if (backend_records.count(p)) {
            node.binding_info = backend_records[p];
            node.selected = false;
        }
        if (node.children != nullptr) {
            auto model = std::dynamic_pointer_cast<slint::VectorModel<TreeItem>>(node.children);
            if (model) {
                for (int i = 0; i < model->row_count(); ++i) {
                    TreeItem child = *model->row_data(i);
                    sync_tree_nodes(child);
                    model->set_row_data(i, child);
                }
            }
        }
    }
};