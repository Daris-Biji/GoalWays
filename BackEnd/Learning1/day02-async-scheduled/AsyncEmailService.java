package com.example.auth.async_scheduled_demo;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class AsyncEmailService {

    // @Async — метод выполняется в отдельном потоке, не блокируя вызывающий код
    // Вызывающий поток сразу получает управление обратно
    @Async
    public void sendWelcomeEmail(String to) {
        System.out.println("[ASYNC] Отправка email на " + to + " | поток: " + Thread.currentThread().getName());
        try {
            Thread.sleep(2000); // имитация долгой отправки
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("[ASYNC] Email отправлен на " + to);
    }
}
