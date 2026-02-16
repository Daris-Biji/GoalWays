package com.example.auth.async_scheduled_demo;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class ScheduledTaskService {

    // fixedRate = 10000 — выполняется каждые 10 секунд (в миллисекундах)
    @Scheduled(fixedRate = 10000)
    public void cleanExpiredTokens() {
        System.out.println("[SCHEDULED] Очистка просроченных токенов | " + LocalDateTime.now());
    }

    // cron = "0 0 * * * *" — выполняется каждый час в 00 минут
    @Scheduled(cron = "0 0 * * * *")
    public void hourlyReport() {
        System.out.println("[SCHEDULED] Часовой отчёт | " + LocalDateTime.now());
    }
}
