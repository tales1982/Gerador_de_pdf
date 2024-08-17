/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   gerador_pdf.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tales <tales@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/08/17 17:12:05 by tales             #+#    #+#             */
/*   Updated: 2024/08/17 17:15:29 by tales            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <hpdf.h>
#include <stdio.h>
#include <stdlib.h>

void error_handler(HPDF_STATUS error_no, HPDF_STATUS detail_no, void *user_data) {
    printf("Erro: error_no=%04X, detail_no=%u\n", (unsigned int)error_no, (unsigned int)detail_no);
    exit(1);
}

int main() {
    HPDF_Doc pdf;
    HPDF_Page page;
    HPDF_Font font;
    HPDF_STATUS status;

    // Cria um novo documento PDF
    pdf = HPDF_New(error_handler, NULL);
    if (!pdf) {
        printf("Falha ao criar o PDF.\n");
        return 1;
    }

    // Adiciona uma nova página ao documento
    page = HPDF_AddPage(pdf);
    HPDF_Page_SetSize(page, HPDF_PAGE_SIZE_A4, HPDF_PAGE_PORTRAIT);

    // Define a fonte e o tamanho
    font = HPDF_GetFont(pdf, "Helvetica", NULL);
    HPDF_Page_SetFontAndSize(page, font, 24);

    // Escreve um texto na página
    HPDF_Page_BeginText(page);
    HPDF_Page_TextOut(page, 50, 750, "Hello, World!");
    HPDF_Page_EndText(page);

    // Salva o PDF em um arquivo
    status = HPDF_SaveToFile(pdf, "output.pdf");
    if (status != HPDF_OK) {
        printf("Falha ao salvar o PDF.\n");
        HPDF_Free(pdf);
        return 1;
    }

    // Libera a memória usada pelo documento PDF
    HPDF_Free(pdf);

    printf("PDF criado com sucesso como 'output.pdf'.\n");
    return 0;
}
