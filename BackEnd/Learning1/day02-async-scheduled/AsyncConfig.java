package com.example.auth.async_scheduled_demo;

import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.EnableScheduling;

// @EnableAsync — включает поддержку асинхронных методов (@Async)
// @EnableScheduling — включает поддержку планировщика (@Scheduled)
@Configuration
@EnableAsync
@EnableScheduling
public class AsyncConfig {
}
