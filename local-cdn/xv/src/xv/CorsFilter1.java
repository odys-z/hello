package xv;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebFilter("/CorsFilter")
public class CorsFilter1 implements Filter {

	@Override
	public void init(FilterConfig filterConfig) throws ServletException {
		System.out.println("\n\n---------");
	}

	@Override
	public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
		System.out.println("---------");
		HttpServletResponse httpResponse = (HttpServletResponse) servletResponse;
		httpResponse.addHeader("Access-Control-Allow-Origin", "*,file://,file:");
		filterChain.doFilter(servletRequest, servletResponse);
	}

	@Override
	public void destroy() {

	}
}
