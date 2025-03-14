import { Component } from '@angular/core';
import { ChartConfiguration, ChartType } from 'chart.js';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-dashboard-reports',
  standalone: false,
  templateUrl: './dashboard-reports.component.html',
  styleUrl: './dashboard-reports.component.scss'
})
export class DashboardReportsComponent {

  filterForm: FormGroup;

  private allLabels = ['2020', '2021', '2022', '2023', '2024'];
  private allBarData = [
    { data: [65, 59, 80, 81, 56], label: 'Sales in Million' },
    { data: [28, 48, 40, 19, 86], label: 'Profit Percentage' }
  ];
  private allLineData = [
    { data: [33, 45, 67, 80, 95], label: 'Gross Revenue in Million' },
    { data: [22, 35, 55, 65, 75], label: 'Stock Growth in percentage' }
  ];

  // Chart configs
  public barChartOptions: ChartConfiguration['options'] = { responsive: true };
  public barChartType: ChartType = 'bar';
  public barChartLegend = true;
  public barChartLabels: string[] = [];
  public barChartData: ChartConfiguration<'bar'>['data']['datasets'] = [];

  public lineChartOptions: ChartConfiguration['options'] = { responsive: true };
  public lineChartType: ChartType = 'line';
  public lineChartLegend = true;
  public lineChartLabels: string[] = [];
  public lineChartData: ChartConfiguration<'line'>['data']['datasets'] = [];

  constructor(private fb: FormBuilder) {
    this.filterForm = this.fb.group({
      yearRange: ['all']
    });
    this.applyFilter();
  }
chartClicked($event:any){
console.log('jjjj', $event)
}
  applyFilter() {
    const range = this.filterForm.value.yearRange;

    let sliceIndex = 0;
    if (range === 'last3') {
      sliceIndex = this.allLabels.length - 3;
    }

    const labels = this.allLabels.slice(sliceIndex);
    this.barChartLabels = [...labels];
    this.lineChartLabels = [...labels];

    this.barChartData = this.allBarData.map(series => ({
      ...series,
      data: series.data.slice(sliceIndex)
    }));

    this.lineChartData = this.allLineData.map(series => ({
      ...series,
      data: series.data.slice(sliceIndex)
    }));
  }
}