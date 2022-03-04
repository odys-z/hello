package io.oz.hello.jetty;

import java.lang.reflect.InvocationTargetException;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.servlet.ServletHandler;
import org.eclipse.jetty.servlet.ServletHolder;
import org.eclipse.jetty.webapp.WebAppContext;

import io.odysz.semantic.jprotocol.AnsonBody;
import io.odysz.semantic.jserv.ServPort;
import io.oz.album.tier.Albums;
import javax.servlet.Servlet;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;

public class StartJettyWebserver {

    public static void main(String[] args) throws Exception {
        Server server = new Server(8082);

        ServletHandler handler = new ServletHandler();
//        server.setHandler(handler);
//        handler.addServletWithMapping(ExampleServlet.class, "/exam");
		WebServlet info = Albums.class.getAnnotation(WebServlet.class);
		handler.addServletWithMapping((Class<? extends Servlet>) Albums.class, info.urlPatterns()[0]);

        
//        WebAppContext wacHandler = new WebAppContext();
//        wacHandler.setContextPath("/jserv");
//        wacHandler.setWar("jserv-album");
//        wacHandler.setConfigurationDiscovered(true);

        WebAppContext wacHandler = new WebAppContext();
        wacHandler.setContextPath("/jserv");
        wacHandler.setResourceBase(".");
        registerServlets(wacHandler, AnnotateServlet.class);
        registerServlets(wacHandler, Albums.class);

        wacHandler.addServlet(ExampleServlet.class, "/exam");

        server.setHandler(wacHandler);
        
        server.start();
        server.join();
    }

    private static <R extends AnsonBody> void registerServlets(WebAppContext context, Class<? extends ServPort> type) throws InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException {
		WebServlet info = type.getAnnotation(WebServlet.class);
		for (String pattern : info.urlPatterns()) {
			javax.servlet.Servlet servlet = type.getConstructor().newInstance();
			context.addServlet(new ServletHolder(servlet), pattern);
		}
	}

	static void registerServlets(ServletContextHandler context, Class<? extends HttpServlet> type)
    		throws InstantiationException, IllegalAccessException, InvocationTargetException, NoSuchMethodException {

		WebServlet info = type.getAnnotation(WebServlet.class);
		for (String pattern : info.urlPatterns()) {
			HttpServlet servlet = type.getConstructor().newInstance();
			context.addServlet(new ServletHolder(servlet), pattern);
		}
	}
}
