#pragma once

#include "webview.h"
#include "app-window.h"

#if defined(_WIN32)
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <private/slint_platform_internal.h>
#elif defined(__APPLE__)
// Objective-C runtime headers to talk to Cocoa objects directly from pure C++
#include <objc/message.h>
#include <objc/runtime.h>
#elif defined(__linux__) || defined(__unix__)
#include <gtk/gtk.h>
#endif

inline void set_webview_visible(webview::webview* wv, bool visible) {
    if (!wv) return;
    
    void* window_handle = wv->window().value();
    if (!window_handle) return;

#if defined(_WIN32)
    // Windows: ShowWindow API controls visibility instantly
    ShowWindow(static_cast<HWND>(window_handle), visible ? SW_SHOW : SW_HIDE);

#elif defined(__APPLE__)
    // macOS: wv->window() returns an NSWindow* pointer.
    // We send the selector setIsVisible: to the NSWindow instance via the Obj-C runtime.
    id nswindow = (id)window_handle;
    SEL set_visible_sel = sel_registerName("setIsVisible:");
    
    // objc_msgSend(receiver, selector, argument)
    ((void (*)(id, SEL, BOOL))objc_msgSend)(nswindow, set_visible_sel, visible ? YES : NO);

#elif defined(__linux__) || defined(__unix__)
    // Linux/POSIX (GTK): wv->window() returns a GtkWindow* pointer.
    GtkWidget* gtk_window = GTK_WIDGET(window_handle);
    if (visible) {
        gtk_widget_show_all(gtk_window);
    } else {
        gtk_widget_hide(gtk_window);
    }
#endif
}

/**
 * Ensures the webview is initialized, sized correctly, and visible.
 * 
 * @param app The Slint application window component pointer
 * @param wv  Reference to the persistent webview unique_ptr
 * @param url The target address to load on initial creation
 */
std::unique_ptr<webview::webview>& show_and_align_webview(App* app, std::unique_ptr<webview::webview>& wv, const std::string& url) {
    if (!app) return wv;

    // 1. Fetch layout constraints dynamically from the Slint component
    int x = static_cast<int>(app->get_web_x());
    int y = static_cast<int>(app->get_web_y());
    int w = static_cast<int>(app->get_web_width());
    int h = static_cast<int>(app->get_web_height());

    if (!wv) {
        auto slint_win_handle = app->window().window_handle();
        HWND hwnd = *reinterpret_cast<HWND*>(&slint_win_handle);
        void* native_win_handle = static_cast<void*>(hwnd);
        
        // Inject structural initialization bindings safely
        wv->init("window.addEventListener('DOMContentLoaded', () => { if(typeof foo === 'function') foo(); });");
        wv->navigate(url);
    } 
    wv->set_size(w, h, WEBVIEW_HINT_NONE);
    set_webview_visible(wv.get(), true);

    return wv;
}