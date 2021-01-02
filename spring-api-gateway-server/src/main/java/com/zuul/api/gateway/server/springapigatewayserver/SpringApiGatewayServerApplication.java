package com.zuul.api.gateway.server.springapigatewayserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;

@SpringBootApplication
@EnableZuulProxy
public class SpringApiGatewayServerApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringApiGatewayServerApplication.class, args);
	}

}
